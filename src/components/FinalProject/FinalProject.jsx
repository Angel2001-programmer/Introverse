import { Fragment, createContext, useState } from 'react';
import NavGraph from '../../navigation/NavGraph';
import AccountCreation from '../../components/accountCreation/accountCreation';
import Recommendations from '../../pages/recommendations/recommendations';

// export const UserContext = createContext();
export const SignUpContext = createContext();
export const NewUserContext = createContext();
export const MobileNavContext = createContext();
export const StyleMobileNavContext = createContext();
export const UserContext = createContext();
export const UserNameContext = createContext();

const FinalProject = () => {
  const [isOpened, setIsOpened] = useState(false);
  const [isSignModal, setIsSignModal] = useState(false);
  const [newUser, setNewUser] = useState(false);
  const [isMobileClicked, setIsMobileClicked] = useState(false);
  let [userName, setUserName] = useState("User");

  let style2 = null

    return(
      <Fragment>
      <UserNameContext.Provider value ={[userName, setUserName]}>
      <StyleMobileNavContext.Provider value={style2}>
      <MobileNavContext.Provider value={[isMobileClicked, setIsMobileClicked]}>
      <NewUserContext.Provider value={[newUser, setNewUser]}>
      <SignUpContext.Provider value={[isSignModal, setIsSignModal]}>
      <UserContext.Provider value={[isOpened, setIsOpened]}>
        <AccountCreation/>
        <NavGraph/>
      </UserContext.Provider>
      </SignUpContext.Provider>
      </NewUserContext.Provider>
      </MobileNavContext.Provider>
      </StyleMobileNavContext.Provider>
      </UserNameContext.Provider>
      </Fragment>
    )
}

export default FinalProject;