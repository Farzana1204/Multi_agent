

from app.llm_service import get_llm


def test_case_agent(
    user_story: str,
    requirement_analysis: str,
    acceptance_criteria: str,
    review_result: str
):
    llm = get_llm()
    prompt = f"""
You are an experienced Senior Software QA Engineer
and Test Case Designer.

Your responsibility is to generate detailed software
test cases based on the provided user story and
reviewed acceptance criteria.

ORIGINAL USER STORY:
{user_story}

REQUIREMENT ANALYSIS:
{requirement_analysis}

ACCEPTANCE CRITERIA:
{acceptance_criteria}

REVIEW FEEDBACK:
{review_result}


IMPORTANT RULES:

1. Treat the original user story as the primary source
   of truth.

2. Consider the Review Agent feedback before generating
   test cases.

3. Generate test cases only for requirements supported
   by the original user story.

4. Do not convert unsupported assumptions into confirmed
   requirements.

5. Do not invent password policies, validation rules,
   security mechanisms, or business rules.

6. Clearly identify test scenarios that require
   clarification from the Business Analyst or Product Owner.

7. Include positive, negative, and edge-case scenarios
   wherever applicable.

8. Every test case must have a unique Test Case ID.

9. Every test case must have a clear title, preconditions,
   test steps, test data, and expected result.

10. Expected results must be traceable to supported
    requirements.

11. If expected behavior is not specified, mark it as
    "Requires Clarification" instead of inventing an
    expected result.


OUTPUT FORMAT:

Section 1: Positive Test Cases

Section 2: Negative Test Cases

Section 3: Edge Case Test Cases

Section 4: Scenarios Requiring Clarification

For each test case, provide:

- Test Case ID
- Test Case Title
- Requirement Reference
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Test Case Status:
  Confirmed / Requires Clarification


FINAL VALIDATION:

- Avoid duplicate test cases.
- Do not invent unsupported requirements.
- Ensure test steps are understandable.
- Ensure expected results are traceable.
- Clearly separate confirmed behavior from assumptions.
- A test case must not be marked Confirmed merely because
  the Review Agent approved it.
- Independently compare every test step and expected result
  against the original user story.
- If a test case contains even one unsupported workflow
  step or expected behavior, mark it as Requires Clarification.
- Do not assume that a password reset page, reset link,
  new password confirmation, error message, or automatic
  login exists.
- Do not generate detailed implementation-specific test
  steps when the reset workflow has not been defined.

Return exactly the four sections.
"""
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    from pathlib import Path
    project_root = Path(__file__).resolve().parents[1]
    story_file = project_root / "sample_data" / "user_story.txt"
    user_story = story_file.read_text(encoding="utf-8")
    
    # Temporary sample inputs for independent testing
    requirement_analysis = """
    Registered customers need to reset their password
    using their registered email address.

    The exact reset mechanism requires clarification.
    """

    acceptance_criteria = """
    1. A registered customer can initiate a password
       reset using their registered email address.
    """

    review_result = """
    The acceptance criterion is supported by the
    original user story.

    The email notification mechanism, reset link,
    password complexity rules, and automatic login
    are not confirmed requirements.
    """
    
    
    test_case = test_case_agent(
        user_story,
        requirement_analysis,
        acceptance_criteria,
        review_result
        
    )
    print("\nGenerated Test Case:\n")
    print(test_case)
    