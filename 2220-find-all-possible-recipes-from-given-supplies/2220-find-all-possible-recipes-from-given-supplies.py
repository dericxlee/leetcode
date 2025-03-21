class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        degrees = defaultdict(int)
        graph = defaultdict(list)
        procured = set(supplies)
        result = []

        queue = deque(supplies)

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
            degrees[recipe] = len(ingredients[i])
        
        while queue:
            supply = queue.popleft()

            if supply in degrees:
                result.append(supply)

            for recipe in graph[supply]:
                degrees[recipe] -= 1
            
                if degrees[recipe] == 0:
                    queue.append(recipe)
        
        return result
                     
