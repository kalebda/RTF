from fastapi import APIRouter, Form
from src.handlers.json_parser import JSONParser

router = APIRouter()


@router.post("/parse", response_model=str, tags=["Parser"])
async def parse_json(
    editor_template: str = Form(
        ...,
        description="template editor-js json",
    ),
):
    parsed = JSONParser()
    template = parsed.parse_json(editor_template)
    return template
