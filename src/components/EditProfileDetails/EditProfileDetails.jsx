import styles from './EditProfileDetails.module.css';
import editProfile from '../../assets/images/editProfile.svg';
import React, { useEffect, useState } from 'react';
import httpClient from '../../httpClient';
import { useSelector } from 'react-redux';
import { selectCurrentUser } from '../../redux/slices/userSlice';
import EditInput from '../EditInput/EditInput';

// Have added an API call ish but no idea how to get it into the profile box or how to convert the profile box to view rather than edit, tried to copy recommendations.js
// Think would be cool to have the component as view only initially with an "edit" button, that then allows you to make a put or post request to edit certain fields

const EditPosts = () => {
  const user = useSelector(selectCurrentUser);
  const [userDetails, setUserDetails] = useState({
    first_name: null,
    last_name: null,
    email: null,
    date_of_birth: null,
    interests: null,
  });
  const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY');
  console.log(token);
  // let editable = true;
  const [userValues, setUserValues] = useState({
    first_name: 'ANGEL',
    last_name: '',
    username: '',
    email: '',
    password: '',
  });

  // 	useEffect(() => {
  //     fetch("http://localhost:5000/user/current_user/", {headers: {"Authorization": `Bearer ${JSON.parse(token)}`}})
  //     .then(res => res.json())
  //     .then(data => {
  //       console.log(data)
  //     })
  //     .catch(error => console.log(error))
  //     }, [token]
  //     );

  // const fetchSecretData = () => {
  //   const URL = "http://localhost:5000/user/current_user/"
  //   const headers = {"Authorization": `Bearer ${JSON.parse(token)}`};
  //   fetch(URL, {headers})
  //   .then(response => response.json())
  //   .then(data => console.log(data));
  // }
  // fetchSecretData()

  //   useEffect(() => {
  //     const getAPI = async () => {
  //       try {
  //         const response = await httpClient.get("http://localhost:5000/user/current_user/", {headers: {"Authorization": `Bearer ${JSON.parse(token)}`}});
  //         console.log(response.data)
  //       } catch(error) {
  //       console.log(error)
  //     }
  //     };
  //     getAPI()
  //   }, [user.name, token]);

  useEffect(() => {
    const getAPI = async () => {
      try {
        const response = await httpClient.get(
          'http://localhost:5000/user/members/' + user.name
        );
        setUserDetails((ud) => (ud = response.data));
        console.log(userDetails);
      } catch (error) {
        console.log(error);
      }
    };
    getAPI();
  }, [user.name]);

  return (
    <form
      className={styles.EditAccountform}
      onSubmit={(e) => {
        e.preventDefault();
        alert('Changes submitted!');

        return setUserValues({
          first_name: '',
          last_name: '',
          username: '',
          email: '',
          password: '',
        });
      }}
      onKeyDown={(e) => {
        if (e.key === 'ENTER') return null;
      }}
    >
      <div className={styles.row}>
        <label>FirstName:</label>
        <EditInput
          placeholder={userDetails.first_name}
          editProfile={editProfile}
          type='text'
          value={userValues.first_name}
          onChange={(e) =>
            setUserValues({ ...userValues, first_name: e.target.value })
          }
        />
      </div>
      <div className={styles.row}>
        <label>LastName:</label>
        <EditInput
          placeholder={userDetails.last_name}
          editProfile={editProfile}
          type='text'
          value={userValues.last_name}
          onChange={(e) =>
            setUserValues({ ...userValues, last_name: e.target.value })
          }
        />
      </div>
      <div className={styles.row}>
        <label>UserName:</label>
        <EditInput
          placeholder={user.name}
          editProfile={editProfile}
          type='text'
          value={userValues.username}
          onChange={(e) =>
            setUserValues({ ...userValues, username: e.target.value })
          }
        />
      </div>
      <div className={styles.row}>
        <label>Email:</label>
        <EditInput
          placeholder={userDetails.email}
          editProfile={editProfile}
          type='email'
          value={userValues.email}
          onChange={(e) =>
            setUserValues({ ...userValues, email: e.target.value })
          }
        />
      </div>
      <div className={styles.row}>
        <label>Password:</label>
        <EditInput
          placeholder='Password'
          editProfile={editProfile}
          type='password'
          value={userValues.password}
          onChange={(e) =>
            setUserValues({ ...userValues, password: e.target.value })
          }
        />
      </div>
      <button type='submit'>Submit Changes</button>
    </form>
  );
};

export default EditPosts;
