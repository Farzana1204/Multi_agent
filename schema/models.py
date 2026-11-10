from typing import TypedDict, NotRequired

class QAState(TypedDict):
    user_story: str
    requirement_analysis: NotRequired[str]
    acceptance_criteria: NotRequired[str]
    review_result: NotRequired[str]
    test_case: NotRequired[str]
    