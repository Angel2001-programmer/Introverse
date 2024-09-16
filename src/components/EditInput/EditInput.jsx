import styles from '../EditProfileDetails/EditProfileDetails.module.css';
import { useState } from 'react';

const EditInput = ({ placeholder, value, editProfile, type, onChange }) => {
  const [inputValid, setInputValid] = useState(false);
  return (
    <>
      <input
        className={inputValid ? styles.editInputActive : styles.editInput}
        type={type}
        name='Last Name'
        placeholder={placeholder}
        readOnly={inputValid ? '' : 'readonly'}
        value={value}
        onChange={onChange}
      />
      <img
        className={styles.imageButton}
        src={editProfile}
        alt='edit Password.'
        onClick={() => {
          setInputValid(!inputValid);
          console.log(inputValid);
        }}
      ></img>
    </>
  );
};

export default EditInput;
