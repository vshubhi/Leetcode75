class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            ast_destroyed = False
            while ast < 0 and stack and stack[len(stack)-1]>0: 
                if abs(ast)>abs(stack[len(stack)-1]):
                    del stack[len(stack)-1]
                elif abs(ast)==abs(stack[len(stack)-1]):
                    del stack[len(stack)-1]
                    ast_destroyed = True
                    break
                elif abs(ast)<abs(stack[len(stack)-1]):
                    ast_destroyed = True
                    break
            if not ast_destroyed:
                stack.append(ast)
        return stack

                
        