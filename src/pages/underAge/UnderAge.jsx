import styles from "./UnderAge.module.css";

const UnderAge = () => {
    return(
    <div className={styles.UnderAge}>
    <div className={styles.ErrorContainer}>
    <div className={styles.ErrorModal}>
      <p className={styles.ErrorMessage}>Access to suggestions denied due to age restriction:</p>
      <button onClick={() => window.location.reload()} className={styles.backButton}>Return to Login</button>
      <p className={styles.AdditionalTextBelow}>Please login to your account to confirm your date of birth.</p>
    </div>
  </div>
  </div>
    )
}

export default UnderAge;
