
from fastapi import FastAPI
from pydantic import BaseModel, Field
from workflow.qa_workflow import qa_workflow

# Create FastAPI application
app = FastAPI(
    title="Multi-Agent QA Assistant",
    description="AI-powered requirement analysis and test case generation",
    version="1.0.0"
)


# Define request structure
class UserStoryRequest(BaseModel):
    user_story: str = Field(
        ...,
        min_length=10,
        description="Enter the software user story"
    )


# Create API endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Multi-Agent QA Assistant"}
@app.post("/generate-test-cases")
def generate_test_cases(request: UserStoryRequest):

    # Prepare initial state for LangGraph
    initial_state = {
        "user_story": request.user_story
    }

    # Execute the existing LangGraph workflow
    result = qa_workflow.invoke(initial_state)

    # Return all agent outputs
    return {
        "requirement_analysis": result["requirement_analysis"],
        "acceptance_criteria": result["acceptance_criteria"],
        "review_result": result["review_result"],
        "test_case": result["test_case"]
    }
