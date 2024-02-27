import { Fragment, createContext, useEffect, useState } from 'react';
import NavGraph from '../../navigation/NavGraph';
import AccountCreation from '../../components/accountCreation/accountCreation';
import styles from './FinalProject.module.css';
import Card from '../../UI/Card/card';
import Button from '../../UI/Button/button';
// import { response } from 'express';
import httpClient from '../../httpClient';

// export const UserContext = createContext();
export const SignUpContext = createContext();
export const NewUserContext = createContext();
export const UserContext = createContext();
export const UserNameContext = createContext();

const FinalProject = () => {
  const [isOpened, setIsOpened] = useState(false);
  const [isSignModal, setIsSignModal] = useState(false);
  const [newUser, setNewUser] = useState(false);
  const [isChatRoom, setIsChatRoom] = useState(false);
  const [users, setIsUsers] = useState([]);
  const [otherUser, setOtherUser] = useState('UserName');
  const [userInput, setUserInput] = useState();
  const [messageInput, setMessageInput] = useState();
  const [usersList, setUserList] = useState([]);
  let [userName, setUserName] = useState('User');
  let style2 = null;
  const onChatRoom = () => {
    setIsChatRoom(!isChatRoom);
  };

  useEffect(() => {
    const getMembers = async () => {
      try {
        httpClient({
          method: 'GET',
          url: 'http://localhost:5000/user/members',
        }).then((response) => {
          console.log(response);
          setUserList(response);
        });
      } catch (error) {
        console.log(error);
      }
    };

    getMembers();
  });

  const handleSearchUser = (e) => {
    console.log(e.target.value);
    setUserInput(e.target.value);

    console.log(usersList);

    // Filter method not working will return to this later.
    if (e.target.value.trim().length > 0) {
      // const filtered = usersList.filter((user) =>
      //   user.includes(e.target.value)
      // );
      // setUserList(filtered);
    } else {
      setUserList([]);
    }
  };

  return (
    <Fragment>
      <UserNameContext.Provider value={[userName, setUserName]}>
        <NewUserContext.Provider value={[newUser, setNewUser]}>
          <SignUpContext.Provider value={[isSignModal, setIsSignModal]}>
            <UserContext.Provider value={[isOpened, setIsOpened]}>
              <AccountCreation />
              <NavGraph />
            </UserContext.Provider>
          </SignUpContext.Provider>
        </NewUserContext.Provider>
      </UserNameContext.Provider>
      <div className={styles.messageContainer}>
        {isChatRoom ? (
          <Card UIcolor='#FFFFFF'>
            <input
              className={styles.inputField}
              placeholder='Search UserName'
              value={userInput}
              onChange={handleSearchUser}
            ></input>
            <ul className={styles.listUser}>
              {users.map((name) => (
                <li
                  className={styles.userItem}
                  onClick={() => {
                    setOtherUser(name);
                    setIsUsers([]);
                    setUserName('');
                    setUserInput('');
                    setMessageInput('');
                  }}
                >
                  {name}
                </li>
              ))}
            </ul>
            <p className={styles.profileName}>{otherUser}</p>
            <div className={styles.user1}>
              <Card
                UIcolor='purple'
                width='5px'
              >
                <p className={styles.messageText}>Hello There!</p>
              </Card>
            </div>
            <div className={styles.user2}>
              <Card
                UIcolor='blue'
                width='5px'
              >
                <p className={styles.messageText}>Hi User hows it going?</p>
              </Card>
            </div>
            <div className={styles.sendMessageContainer}>
              <input
                className={styles.inputField}
                placeholder='Type your Message'
                value={messageInput}
                onChange={(e) => {
                  setMessageInput(e.target.value);
                }}
              ></input>
              <Button
                click={() => {
                  console.log(messageInput);
                  setMessageInput('');
                }}
                UIcolor='purple'
                borderColor='rgb(200, 0, 255)'
                text='Send Message'
                height='45px'
                fontSize='18px'
                paddingToTop='5px'
                paddingToBottom='5px'
                dropShadow='2px 1px 5px 2px rgba(200, 0, 255, 0.643)'
              />
            </div>
          </Card>
        ) : null}
        <div
          className={styles.chatBubble}
          onClick={() => onChatRoom()}
        >
          <img
            className={styles.messageIcon}
            src={require('../../assets/icons/message.png')}
            alt='message users'
          />
        </div>
      </div>
    </Fragment>
  );
};

export default FinalProject;
