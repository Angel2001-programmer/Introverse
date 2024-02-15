import { Fragment, useState, React, useEffect, useContext } from 'react';
import styles from './editAccount.module.css';
import NavBar from '../../components/NavBar/navbar';
import DropDownMenu from '../../components/DropDownMenu/dropDownMenu';
import MobileNav from '../../components/MobileNav/MobileNav';
import EditPosts from '../../components/EditPosts/EditPosts';
import EditBanner from '../../components/EditBanner/EditBanner';
import EditDetailsProfile from '../../components/EditProfileDetails/EditProfileDetails';
import httpClient from '../../httpClient';
import { UserNameContext } from '../../components/FinalProject/FinalProject';
import { useSelector } from 'react-redux';
import { selectCurrentUser } from '../../redux/slices/userSlice';

const EditAccount = () => {
  const [isPressed, setIsPressed] = useState(false);
  const [posts, setPosts] = useState(null);
  const [filteredposts, setfilteredposts] = useState(null);

  // Think we can replace the useContext with the useSelector
  const [UserName, setUserName] = useContext(UserNameContext);

  const user = useSelector(selectCurrentUser);

  console.log(UserName);

  let error = null;
  let filteredList = null;

  /* 
  To do
  - Change filtered list to use the user's username in the url, doesn't work on frontend the moment not sure why, if it is because of the filtering
  - ("http://localhost:5000/forum/author/" + user.name)
  - Have uncommented EditDetailsProfile component, will add tasks related to that there
  */

  useEffect(() => {
    const getForms = async () => {
      const res = await httpClient
        .get('http://localhost:5000/forum/all')
        .then((res) => {
          setPosts(res.data);
          filteredList = res.data.filter(
            (list) => list.post_author === user.name
          );
          console.log(filteredList);
          setfilteredposts(filteredList);
          if (filteredList.length === 0) {
            error = <h2>No Posts Yet.</h2>;
            setPosts(null);
          }
        })
        .catch((err) => {
          setPosts(null);
          console.log(err);
          error = <h2>No Posts Yet.</h2>;
        });
    };
    getForms();
  }, []);

  console.log(filteredList);

  return (
    <Fragment>
      <NavBar
        isPressed={isPressed}
        onChangePressed={setIsPressed}
      />
      <MobileNav />
      <DropDownMenu
        isPressed={isPressed}
        setIsPressed={setIsPressed}
      />
      <main className={styles.main}>
        <EditBanner />
        {posts !== null ? (
          <EditPosts data={filteredposts} />
        ) : (
          <div className={styles.NoPosts}>
            <h2>No Posts Yet.</h2>
          </div>
        )}
        <EditDetailsProfile />
      </main>
    </Fragment>
  );
};

export default EditAccount;
