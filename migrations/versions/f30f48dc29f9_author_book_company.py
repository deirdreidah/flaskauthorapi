"""author,book,company

Revision ID: f30f48dc29f9
Revises: 
Create Date: 2025-02-27 22:37:54.386963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f30f48dc29f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('contact', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=8), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('author_id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email')
    )
    op.create_table('books',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('price', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('isbn', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('no_of_pages', sa.String(length=5), nullable=False),
    sa.Column('price_unit', sa.String(length=20), nullable=False),
    sa.Column('publication_date', sa.String(length=35), nullable=False),
    sa.Column('format', sa.String(length=50), nullable=False),
    sa.Column('genre', sa.String(length=50), nullable=False),
    sa.Column('language', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('book_id'),
    sa.UniqueConstraint('isbn')
    )
    op.create_table('companies',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('origin', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('contact', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('company_id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companies')
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###
