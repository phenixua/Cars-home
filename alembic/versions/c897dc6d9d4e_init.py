"""Init

Revision ID: c897dc6d9d4e
Revises: 
Create Date: 2024-05-06 23:01:26.580845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c897dc6d9d4e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('credit', sa.Float(), nullable=True),
    sa.Column('plate', sa.String(length=32), nullable=False),
    sa.Column('model', sa.String(length=128), nullable=True),
    sa.Column('ban', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate')
    )
    op.create_table('parking_rates',
    sa.Column('rate_per_hour', sa.Float(), nullable=True),
    sa.Column('rate_per_day', sa.Float(), nullable=True),
    sa.Column('number_of_spaces', sa.Integer(), nullable=True),
    sa.Column('number_free_spaces', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pictures',
    sa.Column('find_plate', sa.String(length=32), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('cloudinary_public_id', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('find_plate')
    )
    op.create_table('users',
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=150), nullable=False),
    sa.Column('telegram_id', sa.String(length=50), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('role', sa.Enum('admin', 'user', name='role'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('blacklisted_tokens',
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('history',
    sa.Column('entry_time', sa.DateTime(), nullable=True),
    sa.Column('exit_time', sa.DateTime(), nullable=True),
    sa.Column('parking_time', sa.Float(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('picture_id', sa.Integer(), nullable=False),
    sa.Column('rate_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ),
    sa.ForeignKeyConstraint(['rate_id'], ['parking_rates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_car_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_car_association')
    op.drop_table('history')
    op.drop_table('blacklisted_tokens')
    op.drop_table('users')
    op.drop_table('pictures')
    op.drop_table('parking_rates')
    op.drop_table('cars')
    # ### end Alembic commands ###
