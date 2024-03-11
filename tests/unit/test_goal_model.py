from app.models import User


def test_it_creates_goal():
    # arrange
    user = User.query.first()
    # act
    goal = user.create_goal("SomeGoal")
    # assert
    assert goal.text == "SomeGoal"


def test_it_creates_action():
    # arrange
    user = User.query.first()
    # act
    goal = user.create_goal("SomeGoal")
    goal_action = goal.create_action("SomeAction")
    # assert
    assert goal_action.text == "SomeAction"
    assert goal_action in goal.base_actions.all()


def test_it_gets_goal_user():
    # arrange
    user = User.query.first()
    # act
    goal = user.create_goal("SomeGoal")
    # assert
    assert goal.user == user


def test_it_marks_as_complete():
    # arrange
    user = User.query.first()
    # act
    goal = user.create_goal("SomeGoal")
    goal.mark_as_complete()
    # assert
    assert goal.completed is not None


# TODO - 2
def test_it_sets_correct_percentage_complete():
    pass
