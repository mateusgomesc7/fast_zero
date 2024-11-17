from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='test', email='email@email.com', password='test')

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'email@email.com')
    )

    assert result.username == 'test'
