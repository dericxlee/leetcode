class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * (forget - 1)
        people += [1]
        n-=1

        while n > 0:
            people.pop(0)
            secrets = sum(people[0:forget - delay])
            people.append(secrets)
            n-=1

        return sum(people) % (10**9 + 7) 

