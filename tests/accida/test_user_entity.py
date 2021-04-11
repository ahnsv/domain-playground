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
