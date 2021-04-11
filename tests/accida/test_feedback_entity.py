from models.accida.feedback.entity import Feedback
from models.accida.user.entity import User
from models.accida.model.entity import Model
from sqlalchemy.orm.session import Session


def test_feedback_creation(accida_session: Session):
    test_user = accida_session.query(User).filter_by(name="test").first()
    assert test_user is not None

    test_model = accida_session.query(Model).filter_by(name="accida").first()
    assert test_model is not None

    feedback1 = Feedback(user_id=test_user.id, model_id=test_model.id)
    accida_session.add(feedback1)
    accida_session.commit()
