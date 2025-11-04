"""añadir conversacion_id_Chatlog

Revision ID: 95ec8e1aebdf
Revises: d96ed5a6cbc3
Create Date: 2025-11-03 16:09:54.424710

"""
from alembic import op
import sqlalchemy as sa


revision = '95ec8e1aebdf'
down_revision = 'd96ed5a6cbc3'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('chat_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('conversacion_id', sa.String(length=64), nullable=False))
        batch_op.create_index(batch_op.f('ix_chat_logs_conversacion_id'), ['conversacion_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_chat_logs_created_at'), ['created_at'], unique=False)



def downgrade():
    with op.batch_alter_table('chat_logs', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_chat_logs_created_at'))
        batch_op.drop_index(batch_op.f('ix_chat_logs_conversacion_id'))
        batch_op.drop_column('conversacion_id')
