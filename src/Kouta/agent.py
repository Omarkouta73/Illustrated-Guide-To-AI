class Kouta:
    def __init__(self):
        self.llm = None
        self.memory = None
        self.tools = None
        self.plan = None

    def run(self, task: str)-> str:
        self.memory = []
        return self.one_loop(task)

    def one_loop(self, task):
        goal = self._observe(task)
        prompt = self._prompt_builder(goal)
        action = self._llm_call(prompt) # {'action': 'tool_call', 'tool_call': {'tool_name': '...', 'args': {...}}}
        result = self._execute_action(action)
        self.memory.append("...") # chapter04

        return result

    def _observe(self, task):
        return f"Recieved task: {task}"

    def _prompt_builder(self, goal):
        return f"Prompt for {goal}"

    def _llm_call(self, prompt):
        return f"Processing the prompt... \
            {prompt}"
    
    def _execute_action(self, action):
        return f"Executing {action}"
    