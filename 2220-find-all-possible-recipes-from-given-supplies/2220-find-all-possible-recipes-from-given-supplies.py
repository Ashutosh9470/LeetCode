from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = defaultdict(list) 
        indegree = {} 
        available = set(supplies)
        result = []

        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        queue = deque(supplies)

        while queue:
            item = queue.popleft()
            if item not in graph:
                continue

            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result