import { Fragment, useState, useEffect } from 'react';
import NavBar from '../../components/NavBar/navbar';
import styles from './forum.module.css';
import Card from '../../UI/Card/card';
import ForumItem from '../../components/ForumItem/ForumItem';
import introduce from '../../assets/images/logos/introduce.png';
import anime from '../../assets/images/logos/anime.png';
import gaming from '../../assets/images/logos/joystick.png';
import books from '../../assets/images/logos/books_3771417.png';
import manga from '../../assets/images/logos/manga.png';
import Button from '../../UI/Button/button';
import { Link } from 'react-router-dom';
import DropDownMenu from '../../components/DropDownMenu/dropDownMenu';
import httpClient from '../../httpClient';
// import api from "../../jsonAPI/posts.json";
import axios from 'axios';
import { useSelector } from 'react-redux';
import { selectCurrentUser } from '../../redux/slices/userSlice';

export default function Forum() {
  const [isClicked, setIsClicked] = useState(false);
  const [postContent, setPostContent] = useState('');
  const [isPost, setIsPost] = useState(false);
  const [title, setTitle] = useState('');
  const [loaded, setIsLoaded] = useState(false);
  const [newPost, setIsNewPost] = useState();
  const [endpoint, setEndPoint] = useState('');
  const [isPressed, setIsPressed] = useState(false);
  const [posts, setPosts] = useState([]);
  // const [filteredposts, setfilteredposts] = useState([]);
  // const currDate = new Date().toLocaleString('en-UK', { hour12: true }); Date and Time.
  // const currDate = new Date().toLocaleDateString('en-GB');
  // let endpoint = '';
  const user = useSelector(selectCurrentUser);

  let postID = null;

  let error = '';
  // let APIres = [];

  let timeStamp = new Date().toISOString().slice(0, 19).replace('T', ' ');

  const list = [
    { icon: introduce, title: 'Introduce' },
    { icon: anime, title: 'Anime' },
    { icon: gaming, title: 'Games' },
    { icon: books, title: 'Books' },
    { icon: manga, title: 'Manga' },
  ];

  const forumHandler = (category) => {
    setTitle(category.title);
    setIsClicked(true);
    // console.log("Clicked");
    // console.log(category);
    setEndPoint(category.title);
    console.log('endpoint: ' + endpoint);
    // filterArray(category.title);
  };

  const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY');
  console.log(token);

  const submitPost = async () => {
    httpClient({
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${JSON.parse(token)}`,
      },
      url: 'http://127.0.0.1:5000/forum/all',
      data: {
        post_id: Number(postID + 1),
        post_content: postContent,
        post_category: title,
        post_author: user.name,
        post_date: timeStamp,
      },
    })
      .then((response) => {
        // console.log(response)
        setIsNewPost(!newPost);
        // setfilteredposts([...filteredposts, response]);
        // filterArray(title);
        // console.log(filteredposts)
        alert('Post Added!, \n please refresh browser.');
      })
      .catch((error) => {
        if (error.response) {
          // console.log(error.response)
          // console.log(error.response.status)
          // console.log(error.response.headers)
          setIsNewPost(false);
          if (error.response.status === 401) {
            alert('Invalid Post');
          }
        }
      });
  };

  console.log('date: ' + timeStamp);

  // console.log(posts)

  // Post request needs to be implemented
  const createPost = () => {
    setIsPost(true);
  };

  const postHandler = (e) => {
    setPostContent(e.target.value);
  };

  useEffect(() => {
    // console.log(newPost);
    // console.log(posts);
    const getForms = async (ep) => {
      const res = await httpClient
        .get(`http://localhost:5000/forum/category/${ep}`)
        .then((res) => {
          // APIres = res.data;
          setPosts(res.data);
          console.log('api response: ' + posts);
        })
        .catch((err) => {
          setPosts([]);
          console.log(err);
          error = <h2>No Posts Yet.</h2>;
        });
    };
    if (endpoint !== '') {
      getForms(endpoint);
    }
  }, [endpoint, newPost]);

  // const filterArray = (category) => {
  //   console.log(category);
  //   postID = posts[posts.length - 1].post_id;
  //   let filterList = posts.filter((list) => list.post_category === category);
  //   setfilteredposts(filterList);
  //   console.log(posts);
  // };

  return (
    <Fragment>
      {isPost ? (
        <div id='modalBG'>
          <Card
            UIcolor='#D9D9D9'
            borderRadius='10px'
          >
            <div className={styles.container}>
              <div className={styles.titleContainer}>
                <h3
                  className={styles.close}
                  onClick={() => setIsPost(false)}
                >
                  X
                </h3>
                <h3 className={styles.title}>Create Post</h3>
              </div>
              <h3 className={styles.title}>{title}</h3>
              <textarea
                className={styles.post}
                type='text'
                placeholder='Post content goes here....'
                name='postContent'
                value={postContent}
                onChange={(e) => postHandler(e)}
              />
              <div className={styles.buttonContainer}>
                <Button
                  UIcolor='linear-gradient(#D000AF, #9000A8)'
                  paddingToLeft='60px'
                  paddingToRight='60px'
                  borderColor='purple'
                  dropShadow='5px 5px 5px #D000AF80'
                  text='Submit Post'
                  click={(e) => {
                    setIsPost(false);
                    submitPost();
                    setPostContent('');
                    setIsNewPost(true);
                    // filterArray(title);
                    // setTitle("")
                  }}
                />
              </div>
            </div>
          </Card>
        </div>
      ) : null}
      <NavBar
        isPressed={isPressed}
        onChangePressed={setIsPressed}
      />
      <Link
        className='link'
        to='/finalProject'
      >
        <DropDownMenu
          isPressed={isPressed}
          setIsPressed={setIsPressed}
        />
      </Link>
      <main className={styles.main}>
        {!isClicked ? (
          <div className={styles.column}>
            <Card
              UIcolor='#D9D9D9'
              borderRadius='10px'
            >
              <h2>Forums</h2>
            </Card>
            <Card
              UIcolor='#D9D9D9'
              borderRadius='10px'
            >
              <div className={styles.column}>
                {list.map((category) => (
                  <ForumItem
                    key={category.title}
                    icon={category.icon}
                    title={category.title}
                    isComments={false}
                    click={() => {
                      forumHandler(category);
                    }}
                  />
                ))}
              </div>
            </Card>
          </div>
        ) : (
          <div className={styles.column}>
            <Card
              UIcolor='#D9D9D9'
              borderRadius='10px'
            >
              <div className={styles.row}>
                <h2
                  className={styles.arrow}
                  onClick={() => {
                    setIsClicked(false);
                    setPosts(posts);
                    setTitle('');
                  }}
                >
                  ←
                </h2>
                <h2>{title}</h2>
                <h2
                  className={styles.createpost}
                  onClick={() => {
                    createPost();
                  }}
                >
                  Create Post
                </h2>
              </div>
            </Card>
            <Card
              UIcolor='#D9D9D9'
              borderRadius='10px'
              overflowY='scroll'
            >
              <div className={styles.column}>
                {error}
                {posts.length !== 0 ? (
                  posts.map((category) => (
                    <ForumItem
                      key={category.post_id}
                      icon=''
                      title={category.post_content}
                      userName={category.post_author}
                      isComments={true}
                    />
                  ))
                ) : (
                  <div className={styles.NoPosts}>
                    <h2>No Posts Yet.</h2>
                  </div>
                )}
              </div>
            </Card>
          </div>
        )}
      </main>
    </Fragment>
  );
}
