from models.accida.user.entity import User, UserRole, UserRoleEnum
from sqlalchemy.orm import Session


def test_user_creation(db_session: Session):

    next_user = User(name="test3", hashed_pw="1243123")
    db_session.add(next_user)
    db_session.commit()

    selected_user = db_session.query(User).filter_by(name="test3").first()

    admin_role = UserRole(name=UserRoleEnum.ADMIN)
    db_session.add(admin_role)
    db_session.commit()

    selected_user.update_roles([admin_role])
    db_session.commit()

    assert selected_user.hashed_pw == "1243123"
    assert selected_user.roles[0].name == UserRoleEnum.ADMIN
