"""empty message

Revision ID: dabc80f65b6b
Revises: 544daed47f84
Create Date: 2023-12-04 19:59:08.255104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dabc80f65b6b'
down_revision = '544daed47f84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_spectra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('frequency', sa.PickleType(), nullable=True),
    sa.Column('intensity', sa.PickleType(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_spectra', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_spectra_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_spectra', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_spectra_timestamp'))

    op.drop_table('user_spectra')
    # ### end Alembic commands ###
