from langchain_ollama import ChatOllama


from app.llm_service import get_llm
from my_agents.requirement_agent import requirement_agent
def generate_acceptance_criteria(user_story: str, requirement_agent: str):
    llm = get_llm()
    
    prompt = f"""
    
    You are an experienced Business Analyst, Senior QA Engineer,
and Software Testing Specialist.

Your task is to carefully analyze the given user story and
generate accurate, clear, and testable acceptance criteria.

USER STORY:
{user_story}

REQUIREMENT ANALYSIS:
{requirement_agent}

- Use the Requirement Analyst output to understand
  the explicit requirements, implied requirements,
  and missing information.

- The original user story is the primary source of truth.

- Do not blindly accept every statement from the
  Requirement Analyst.

- If the Requirement Analyst introduces an assumption
  that is not supported by the original user story,
  do not treat it as a confirmed requirement.

- Generate confirmed acceptance criteria only from
  requirements supported by the original user story.


IMPORTANT RULES:

1. Understand the user story before generating acceptance criteria.

2. Generate confirmed acceptance criteria ONLY from information
   explicitly stated or directly implied by the user story.

3. Every confirmed acceptance criterion must be traceable
   to a specific statement in the user story.

4. NEVER invent business rules, functional requirements,
   validation limits, security policies, time limits,
   attempt limits, or system behavior.

5. Do not introduce additional functionality that is not
   mentioned or directly implied by the user story.

6. Do not treat common industry practices or security best
   practices as confirmed business requirements.

7. Do not assume the existence of:
   - Audit logging
   - Confirmation emails
   - Two-factor authentication
   - Security questions
   - Password complexity rules
   - Account locking
   - Automatic login
   - Link expiration
   unless explicitly mentioned in the user story.

8. Never recommend storing or logging plaintext passwords
   or other sensitive credentials.

9. If a requirement is unclear or incomplete, do not guess.
   Mention it under Clarifications Required.

10. Separate confirmed requirements from suggested QA scenarios.

11. Suggested QA scenarios may include useful negative,
    boundary, and failure scenarios even when their expected
    behavior is not specified.

12. Clearly identify scenarios that require business
    confirmation. Do not present assumptions as facts.

13. Avoid duplicate acceptance criteria and duplicate
    test scenarios.

14. Use simple, professional, and unambiguous language.

15. Every acceptance criterion must be independently
    understandable and testable.
16. Do not automatically convert suggested security practices
    into confirmed acceptance criteria.

17. Do not assume that the system sends emails, generates
    unique links, automatically logs in users, or maintains
    audit logs unless the user story explicitly states this.

18. Do not invent expected system behavior for edge cases.
    Describe what needs to be tested and mark the expected
    behavior as requiring clarification when undefined.

19. Every clarification question must be directly related
    to a requirement or scenario in the original user story.

20. Do not introduce unrelated functionality such as account
    locking, login attempts, or two-factor authentication
    unless the user story provides a reason to consider it.

21. Distinguish between:
    - Functional requirements
    - Implied requirements
    - Suggested security tests
    - Business rules requiring confirmation.

22. Never state that a system generates a new password
    when the user story describes the customer resetting
    their own password.

23. For each confirmed acceptance criterion, internally
    verify its supporting evidence in the original story.
    If no supporting evidence exists, move it out of
    Confirmed Acceptance Criteria.    


EDGE CASE ANALYSIS:

Identify relevant edge cases by considering:

- Empty or null inputs.
- Invalid input formats.
- Leading and trailing spaces.
- Special characters.
- Minimum and maximum input lengths.
- Boundary conditions.
- Duplicate submissions.
- Repeated user actions.
- Expired or invalid links, if applicable.
- Reuse of previously used links, if applicable.
- Network failures or interrupted operations.
- Unexpected system responses.
- Missing or unavailable data.

IMPORTANT:
Do not assume that every edge case is applicable.
Include only relevant edge cases for the given user story.
If expected behavior is not defined, mark it as requiring
business clarification.


OUTPUT FORMAT:

Section 1: Confirmed Acceptance Criteria

- Generate numbered acceptance criteria.
- Include only requirements explicitly stated or directly
  implied by the user story.
- Ensure every criterion is clear, specific, and testable.
- Do not include unsupported assumptions.


Section 2: Suggested QA Scenarios

Divide this section into:

A. Positive Scenarios
- Identify scenarios where the functionality should work
  successfully.

B. Negative Scenarios
- Identify invalid inputs or unsuccessful operations.

C. Assumptions Requiring Confirmation
- Mention useful scenarios that depend on business rules
  that are not defined in the user story.

Do not invent expected system behavior.


Section 3: Edge Cases

- List relevant edge cases separately.
- Include boundary conditions, unusual inputs,
  repeated actions, and failure scenarios.
- Explain what needs to be tested.
- If expected behavior is unknown, explicitly state
  "Expected behavior requires business clarification."
- Do not classify suggested edge cases as confirmed
  acceptance criteria.


Section 4: Clarifications Required

List questions that must be answered by the Business Analyst
or Product Owner.

Consider:
- Missing functional rules.
- Validation requirements.
- Error handling.
- Security-related requirements.
- Boundary conditions.
- Unclear expected behavior.

Only include questions relevant to this user story.
Avoid repeating the same clarification in multiple ways.


Section 5: Requirement Coverage

- Identify the main requirements in the original user story.
- Map each requirement to its corresponding confirmed
  acceptance criterion.
- Identify any requirement that has not been covered.
- Do not claim complete coverage if any requirement is missing.
- Do not include suggested scenarios as confirmed
  requirement coverage.


FINAL VALIDATION BEFORE RESPONDING:

Before generating the final answer, verify:

1. Are all confirmed acceptance criteria supported by
   the original user story?
2. Have any business rules been invented?
3. Are suggested QA scenarios clearly separated
   from confirmed requirements?
4. Are relevant edge cases included?
5. Are undefined behaviors marked for clarification?
6. Are any acceptance criteria duplicated?
7. Is every original requirement covered?

If any confirmed criterion is unsupported by the user story,
remove it or move it to Suggested QA Scenarios or
Clarifications Required.

Return the output using the five sections above.
"""


    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    from pathlib import Path
    project_root = Path(__file__).resolve().parents[1]
    story_file = project_root/"sample_data"/"user_story.txt"
    user_story = story_file.read_text(encoding="utf-8")
    print("Original User Story: ", user_story)
    
    print("Requirement Analysis: ", requirement_agent)
    print("\nRequirement analysis completed\n")
    print("\n Running acceptance criteria\n")
    # print("\n Generating acceptance criteria \n")
    acceptance_criteria = generate_acceptance_criteria(user_story, requirement_agent)
    print("Generating acceptance criteria:\n ",acceptance_criteria)
    

    
    
    