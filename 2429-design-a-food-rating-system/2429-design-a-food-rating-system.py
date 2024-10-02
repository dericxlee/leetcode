class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = {}
        self.food_type = {}
        self.cuisine_ratings = {}
        
        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i]
            self.food_type[foods[i]] = cuisines[i]

            if cuisines[i] not in self.cuisine_ratings:
                self.cuisine_ratings[cuisines[i]] = []

            heapq.heappush(self.cuisine_ratings[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating

        heapq.heappush(self.cuisine_ratings[self.food_type[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:

        while self.cuisine_ratings[cuisine]:
            rating, food = self.cuisine_ratings[cuisine][0]
            if self.food_ratings[food] == -rating:
                return food
            heapq.heappop(self.cuisine_ratings[cuisine])
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)