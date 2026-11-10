from app.llm_service import get_llm


def requirement_agent(user_story:str):
    llm = get_llm()
    prompt = f"""
You are an experienced Business Analyst and Requirements Analyst.

Your task is to analyze the given user story and identify
its requirements, ambiguities, and missing information.

USER STORY:
{user_story}

IMPORTANT RULES:

1. Analyze only the information provided in the user story.
2. Do not invent business rules or functional requirements.
3. Separate explicitly stated requirements from implied requirements.
4. Every explicit requirement must be traceable to the original story.
5. For implied requirements, explain why they are implied.
6. Do not assume technical implementation details.
7. Do not introduce unrelated features or functionality.
8. If information is missing, identify it as an ambiguity.
9. Do not generate acceptance criteria or test cases.
10. Use simple and professional language.
11. Do not confuse the business objective with an explicit
    functional requirement.
12. Supporting statements must quote the exact part of the
    user story that supports the requirement.
13. Do not interpret a general security objective as proof
    of a specific security implementation.
14. Do not assume a reset link, OTP, email notification,
    security question, or authentication mechanism.
15. Identify the required functionality without deciding
    how it must be technically implemented.
16. Out-of-scope assumptions must include plausible
    functionality that is not specified in the story.
    Do not return "None identified" when assumptions exist.
17. Do not duplicate the business objective as a separate
    functional requirement.
18. For every explicit requirement, quote the exact
    supporting statement that describes the functionality.
19. The phrase "so that" generally describes the business
    benefit. Do not use it as evidence for a functional
    requirement unless it explicitly describes functionality.
20. Do not classify implementation choices such as email
    notifications, OTP, reset links, or account tracking
    as implied requirements.
21. Do not interpret account access or account management
    as a requirement to track user activity.
22. Identify the need for security without assuming
    a particular security implementation.    

OUTPUT FORMAT:

Section 1: User Story Understanding
- Explain the purpose of the user story.
- Identify the user.
- Identify the user's goal.
- Identify the business benefit.

Section 2: Explicit Requirements
- Extract requirements directly stated in the user story.
- Include the supporting statement from the original story.
- Do not add assumptions.

Section 3: Implied Requirements
- Identify requirements reasonably implied by the story.
- Explain why each requirement is implied.
- Do not treat assumptions as confirmed requirements.

Section 4: Ambiguities and Missing Information
- Identify unclear or incomplete requirements.
- List questions that should be clarified with the
  Business Analyst or Product Owner.
- Keep questions relevant to the user story.

Section 5: Out-of-Scope Assumptions
- Identify functionality that might seem relevant but
  is not supported by the user story.
- Explain why it cannot be considered a confirmed requirement.

FINAL VALIDATION:

Before responding, verify:
1. Every explicit requirement comes from the original story.
2. Implied requirements are clearly identified.
3. No unsupported business rules have been introduced.
4. Clarification questions are relevant.
5. No acceptance criteria or test cases are generated.

Return exactly the five sections above.
"""
    response = llm.invoke(prompt)
    return response.content
if __name__ == "__main__":
    from pathlib import Path
    
    project_root = Path(__file__).resolve().parents[1]
    story_file = project_root / "sample_data" / "user_story.txt"
    user_story= story_file.read_text(encoding="utf-8")
    print("Original user story:\n", user_story)
    print("\nLoading requirement agent...\n")
    requirement_analysis = requirement_agent(user_story)
    print("Analyzed requirements:\n", requirement_analysis)

