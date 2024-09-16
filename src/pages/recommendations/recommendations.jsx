import styles from './recommendations.module.css';
import React, { Fragment, useEffect } from 'react';
import Button from '../../UI/Button/button';
import { useState } from 'react';
import httpClient from '../../httpClient';
import NavBar from '../../components/NavBar/navbar';
import DropDownMenu from '../../components/DropDownMenu/dropDownMenu';

const Recommendations = () => {
  const tempList = [{ text: 'Anime' }, { text: 'Games' }, { text: 'Books' }];
  const [GenreTitle, setGenreTitle] = useState('');
  const [List, setList] = useState([]);
  const [isClicked, setisClicked] = useState(false);
  const [isPressed, setIsPressed] = useState(false);
  let route = '';

  const formatter = new Intl.NumberFormat('en-UK', {
    style: 'currency',
    currency: 'GBP',

    // These options are needed to round to whole numbers if that's what you want.
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
  });

  const SelectedGenre = (title) => {
    setGenreTitle(title);
    setisClicked(true);
  };

  let listComponent = null;
  try {
    switch (GenreTitle) {
      case 'Anime':
        route = 'anime';
        listComponent = (
          <Fragment>
            {List.map((item) => (
              <div
                key={item.anime_id}
                className={styles.Container}
                style={{ backgroundColor: 'white' }}
              >
                <div className={styles.rowContainer}>
                  <div className={styles.ColumnContainer}>
                    <h3>Name: {item.anime_name}</h3>
                    <h3>Genre: {item.anime_genre}</h3>
                    <h5>Description: {item.anime_script}</h5>
                    <h3>You can find this on {item.where_tw}</h3>
                  </div>
                </div>
              </div>
            ))}
          </Fragment>
        );
        break;
      case 'Books':
        route = 'books';
        listComponent = (
          <Fragment>
            {List.map((item) => (
              <div
                key={item.book_id}
                className={styles.Container}
                style={{ backgroundColor: 'white' }}
              >
                <div className={styles.rowContainer}>
                  <img
                    className={styles.photo}
                    alt='book items'
                    src={item.book_image}
                  />
                  <div className={styles.ColumnContainer}>
                    <h3 className={styles.forumTitle}>
                      Name: {item.book_name}
                    </h3>
                    <h3 className={styles.forumTitle}>
                      Genre: {item.book_genre}
                    </h3>
                    <h5 className={styles.description}>
                      Description: {item.book_script}
                    </h5>
                    <h5 className={styles.forumTitle}>
                      Auther: {item.book_author}
                    </h5>
                    <h5 className={styles.forumTitle}>
                      Price: {formatter.format(item.price)}
                    </h5>
                  </div>
                </div>
              </div>
            ))}
          </Fragment>
        );
        break;
      case 'Games':
        route = 'games';

        listComponent = (
          <Fragment>
            {List.map((item) => (
              <div
                key={item.game_id}
                className={styles.Container}
                style={{ backgroundColor: 'white' }}
              >
                <div className={styles.rowContainer}>
                  <div className={styles.ColumnContainer}>
                    <h3>Name: {item.game_name}</h3>
                    <h3>Genre: {item.game_genre}</h3>
                    <h5>Description: {item.game_script}</h5>
                    <h5>{formatter.format(item.price)}</h5>
                    <h3>You can play on {item.w_console}</h3>
                  </div>
                </div>
              </div>
            ))}
          </Fragment>
        );
        break;
      default:
        listComponent = (
          <h3 className={styles.errorMessage}>
            Something went wrong please try again later!
          </h3>
        );
        break;
    }
  } catch (e) {
    listComponent = (
      <h3 className={styles.errorMessage}>
        Something went wrong please try again later!
      </h3>
    );
  }

  useEffect(() => {
    const getAPI = async () => {
      try {
        const response = await httpClient.get(
          'http://localhost:5000/content/' + route
        );
        setList(response.data);
        console.log(List);
      } catch (error) {
        setList(null);
        console.log(error);
        listComponent = (
          <h3 className={styles.errorMessage}>
            Something went wrong please try again later!
          </h3>
        );
      }
    };
    if (route !== '') {
      getAPI();
    }
  }, [GenreTitle]);

  console.log(listComponent);
  return (
    <div>
      <NavBar
        isPressed={isPressed}
        onChangePressed={setIsPressed}
      />
      <DropDownMenu
        isPressed={isPressed}
        setIsPressed={setIsPressed}
      />
      <div className={styles.Page}>
        {!isClicked ? (
          <div className={styles.Container}>
            {tempList.map((Genre) => (
              <Button
                key={Genre.text}
                text={Genre.text}
                paddingToLeft='25vh'
                paddingToRight='25vh'
                click={() => SelectedGenre(Genre.text)}
              />
            ))}
          </div>
        ) : (
          <Fragment>
            <div className={styles.topMenu}>
              <h2
                className={styles.title}
                onClick={() => setisClicked(false)}
                style={{ cursor: 'pointer' }}
              >
                ←
              </h2>
              <h2 className={styles.title}>{GenreTitle}</h2>
            </div>
            <div className={styles.ContainerMain}>
              {listComponent.props.children.length !== 0 ? (
                listComponent
              ) : (
                <h3 className={styles.errorMessage}>
                  Something went wrong please try again later!
                </h3>
              )}
            </div>
          </Fragment>
        )}
      </div>
    </div>
  );
};
export default Recommendations;
