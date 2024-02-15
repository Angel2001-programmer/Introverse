"""Updated table and column names for content tables to be lowercase

Revision ID: e11b182cd2e2
Revises: 4a803065cd9a
Create Date: 2024-02-14 11:44:06.282191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e11b182cd2e2'
down_revision = '4a803065cd9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('anime', schema=None) as batch_op:
        batch_op.add_column(sa.Column('anime_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('anime_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('anime_genre', sa.String(length=25), nullable=False))
        batch_op.add_column(sa.Column('where_tw', sa.String(length=25), nullable=True))
        batch_op.add_column(sa.Column('anime_script', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('anime_image', sa.String(length=100), nullable=True))
        batch_op.drop_index('Anime_ID')
        batch_op.drop_index('Anime_Image')
        batch_op.drop_index('Anime_Name')
        batch_op.create_unique_constraint(None, ['anime_image'])
        batch_op.create_unique_constraint(None, ['anime_id'])
        batch_op.create_unique_constraint(None, ['anime_name'])
        batch_op.drop_column('Anime_Name')
        batch_op.drop_column('Anime_Script')
        batch_op.drop_column('Anime_Genre')
        batch_op.drop_column('Where_TW')
        batch_op.drop_column('Anime_ID')
        batch_op.drop_column('Anime_Image')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('book_name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('book_author', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('book_genre', sa.String(length=25), nullable=False))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('book_script', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('book_image', sa.String(length=100), nullable=True))
        batch_op.drop_index('Book_ID')
        batch_op.drop_index('Book_Image')
        batch_op.drop_index('Book_Name')
        batch_op.create_unique_constraint(None, ['book_name'])
        batch_op.create_unique_constraint(None, ['book_id'])
        batch_op.create_unique_constraint(None, ['book_image'])
        batch_op.drop_column('Book_ID')
        batch_op.drop_column('Book_Genre')
        batch_op.drop_column('Book_Name')
        batch_op.drop_column('Book_Author')
        batch_op.drop_column('Book_Script')
        batch_op.drop_column('Book_Image')
        batch_op.drop_column('Price')

    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('game_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('game_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('game_genre', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('w_console', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('game_script', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('game_image', sa.String(length=100), nullable=True))
        batch_op.drop_index('Game_ID')
        batch_op.drop_index('Game_Image')
        batch_op.drop_index('Game_Name')
        batch_op.create_unique_constraint(None, ['game_name'])
        batch_op.create_unique_constraint(None, ['game_image'])
        batch_op.create_unique_constraint(None, ['game_id'])
        batch_op.drop_column('Game_Image')
        batch_op.drop_column('Game_ID')
        batch_op.drop_column('Game_Script')
        batch_op.drop_column('W_Console')
        batch_op.drop_column('Price')
        batch_op.drop_column('Game_Name')
        batch_op.drop_column('Game_Genre')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Game_Genre', mysql.VARCHAR(length=30), nullable=False))
        batch_op.add_column(sa.Column('Game_Name', mysql.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('Price', mysql.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('W_Console', mysql.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('Game_Script', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('Game_ID', mysql.INTEGER(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('Game_Image', mysql.VARCHAR(length=100), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('Game_Name', ['Game_Name'], unique=True)
        batch_op.create_index('Game_Image', ['Game_Image'], unique=True)
        batch_op.create_index('Game_ID', ['Game_ID'], unique=True)
        batch_op.drop_column('game_image')
        batch_op.drop_column('game_script')
        batch_op.drop_column('price')
        batch_op.drop_column('w_console')
        batch_op.drop_column('game_genre')
        batch_op.drop_column('game_name')
        batch_op.drop_column('game_id')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Price', mysql.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('Book_Image', mysql.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('Book_Script', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('Book_Author', mysql.VARCHAR(length=30), nullable=False))
        batch_op.add_column(sa.Column('Book_Name', mysql.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('Book_Genre', mysql.VARCHAR(length=25), nullable=False))
        batch_op.add_column(sa.Column('Book_ID', mysql.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('Book_Name', ['Book_Name'], unique=True)
        batch_op.create_index('Book_Image', ['Book_Image'], unique=True)
        batch_op.create_index('Book_ID', ['Book_ID'], unique=True)
        batch_op.drop_column('book_image')
        batch_op.drop_column('book_script')
        batch_op.drop_column('price')
        batch_op.drop_column('book_genre')
        batch_op.drop_column('book_author')
        batch_op.drop_column('book_name')
        batch_op.drop_column('book_id')

    with op.batch_alter_table('anime', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Anime_Image', mysql.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('Anime_ID', mysql.INTEGER(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('Where_TW', mysql.VARCHAR(length=25), nullable=True))
        batch_op.add_column(sa.Column('Anime_Genre', mysql.VARCHAR(length=25), nullable=False))
        batch_op.add_column(sa.Column('Anime_Script', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('Anime_Name', mysql.VARCHAR(length=50), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('Anime_Name', ['Anime_Name'], unique=True)
        batch_op.create_index('Anime_Image', ['Anime_Image'], unique=True)
        batch_op.create_index('Anime_ID', ['Anime_ID'], unique=True)
        batch_op.drop_column('anime_image')
        batch_op.drop_column('anime_script')
        batch_op.drop_column('where_tw')
        batch_op.drop_column('anime_genre')
        batch_op.drop_column('anime_name')
        batch_op.drop_column('anime_id')

    # ### end Alembic commands ###