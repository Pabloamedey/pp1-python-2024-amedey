"""Relaciones VehiculoTipoMarca

Revision ID: 4fd4bfd03ab5
Revises: 6fb139ae6689
Create Date: 2024-06-25 20:25:25.186637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd4bfd03ab5'
down_revision = '6fb139ae6689'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])
        batch_op.create_foreign_key(None, 'tipo', ['tipo_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('marca_id')
        batch_op.drop_column('tipo_id')

    # ### end Alembic commands ###