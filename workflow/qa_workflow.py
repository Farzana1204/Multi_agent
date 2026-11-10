from schema.models import QAState
from my_agents.requirement_agent import requirement_agent
from my_agents.acceptance_criteria_agent import generate_acceptance_criteria
from my_agents.review_agent import review_agent
from my_agents.test_case_agent import test_case_agent
from langgraph.graph import StateGraph, START, END

def requirement_node(state: QAState):
    requirement_analysis = requirement_agent(
        state["user_story"]
    )
    return {
        "requirement_analysis": requirement_analysis
    }
def acceptance_criteria_node(state: QAState):
    acceptance_criteria = generate_acceptance_criteria(
        state["user_story"],
        state["requirement_analysis"]
    )
    return {
        "acceptance_criteria": acceptance_criteria
    }
def review_node(state: QAState):
    review_result = review_agent(
        state["user_story"],
        state["requirement_analysis"],
        state["acceptance_criteria"]
    )    
    return{
        "review_result": review_result
    }

def test_case_node(state: QAState):
    test_case = test_case_agent(
        state["user_story"],
        state["requirement_analysis"],
        state["acceptance_criteria"],
        state["review_result"]
    )
    return {
        "test_case": test_case
    }
    
                                
# create graph
builder = StateGraph(QAState)

#Register the requirement analyst node
builder.add_node("requirement_analyst", requirement_node)
builder.add_node("acceptance_criteria", acceptance_criteria_node)
builder.add_node("review", review_node)
builder.add_node("test_case", test_case_node)

#Define workflow connections
builder.add_edge(START, "requirement_analyst")
builder.add_edge("requirement_analyst", "acceptance_criteria")
builder.add_edge("acceptance_criteria", "review")
builder.add_edge("review", "test_case")
builder.add_edge("test_case", END)

#compile the graph
qa_workflow = builder.compile()

if __name__ == "__main__":
    from pathlib import Path
    project_root = Path(__file__).resolve().parents[1]
    story_file = project_root / "sample_data" / "user_story.txt"
    user_story = story_file.read_text(encoding = 'utf-8')
    
    initial_state = {
        "user_story": user_story
    }
    
    result = qa_workflow.invoke(initial_state)
    
    print("Requirement Analysis Result: ", result["requirement_analysis"])
    print("\nAcceptance Criteria Result: \n", result["acceptance_criteria"])
    print("\nReview Result: \n", result["review_result"])
    print("\nTest Case Result: \n", result["test_case"])
    
