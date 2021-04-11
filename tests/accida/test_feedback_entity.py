from models.accida.feedback.entity import Feedback
from models.accida.user.entity import User
from sqlalchemy.orm.session import Session


def test_feedback_creation(db_session: Session):
    test_user = db_session.query(User).filter_by(name="test").first()
    assert test_user is not None

    feedback1 = Feedback(user_id=test_user.id)
    db_session.add(feedback1)
    db_session.commit()
