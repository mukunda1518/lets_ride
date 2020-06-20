from dataclasses import dataclass

@dataclass
class UserResponseDTO:
    user_id: int
    question_id: int
    user_submitted_option_id: int