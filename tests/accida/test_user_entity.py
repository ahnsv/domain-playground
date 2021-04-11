from models.accida.model.entity import Model
from models.accida.feedback.entity import Feedback
from models.accida.user.entity import User, UserRole, UserRoleEnum
from sqlalchemy.orm import Session


def test_user_creation(accida_session: Session):

    next_user = User(name="test3", hashed_pw="1243123")
    accida_session.add(next_user)
    accida_session.commit()

    selected_user = accida_session.query(User).filter_by(name="test3").first()

    admin_role = UserRole(name=UserRoleEnum.ADMIN)
    accida_session.add(admin_role)
    accida_session.commit()

    selected_user.update_roles([admin_role])
    accida_session.commit()

    assert selected_user.hashed_pw == "1243123"
    assert selected_user.roles[0].name == UserRoleEnum.ADMIN


def test_user_create_feedback(accida_session: Session):
    test_user = accida_session.query(User).filter_by(name="test2").first()
    test_model = (
        accida_session.query(Model)
        .filter_by(name="accida", version="v2.0.0")
        .first()
    )
    next_feedback = Feedback(user_id=test_user.id, model_id=test_model.id)
    test_user.create_feedback(next_feedback)
    accida_session.add(next_feedback)
    accida_session.commit()

    selected_feedback = (
        accida_session.query(Feedback)
        .filter_by(user_id=test_user.id, model_id=test_model.id)
        .first()
    )

    assert selected_feedback is not None
