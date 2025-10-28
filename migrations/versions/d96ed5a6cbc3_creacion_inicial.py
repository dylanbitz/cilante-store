"""Creacion Inicial

Revision ID: d96ed5a6cbc3
Revises: 
Create Date: 2025-10-27 18:54:15.008270

"""
from alembic import op
import sqlalchemy as sa


revision = 'd96ed5a6cbc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('usuarios',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('chat_logs',
    sa.Column('log_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mensaje_usuario', sa.String(length=100), nullable=False),
    sa.Column('respuesta_bot', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['usuarios.user_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('comentarios',
    sa.Column('coment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('contenido', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['usuarios.user_id'], ),
    sa.PrimaryKeyConstraint('coment_id')
    )
    op.create_table('contactos',
    sa.Column('contacto_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('telefono', sa.String(length=13), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['usuarios.user_id'], ),
    sa.PrimaryKeyConstraint('contacto_id'),
    sa.UniqueConstraint('telefono')
    )


def downgrade():
    op.drop_table('contactos')
    op.drop_table('comentarios')
    op.drop_table('chat_logs')
    op.drop_table('usuarios')
