from typing import Optional

from app.models import Goal, User


def _create_goal(name: Optional[str] = "SomeGoal") -> Goal:
    user = User.query.first()
    return user.create_goal(name)


def test_it_creates_subaction():
    # arrange
    goal = _create_goal()
    action_1 = goal.create_action("SomeAction")
    # act
    action_2 = action_1.create_subaction("SomeSubAction")
    # assert
    assert action_2.text == "SomeSubAction"
    assert action_2.parent_action == action_1


# TODO - 1
def test_it_marks_as_complete():
    pass


# TODO - 1
def test_it_marks_as_not_complete():
    pass
