import styles from "./Landing.module.css"
import dropArrow from "../../assets/images/logos/drop_Icon.svg"

const Landing = () => {
    return(
    <main className={styles.main}>
        <div className={styles.rowHome}>
        <div className={styles.containerHeading}>
        <h1 className={styles.textHeading}>Find your community</h1>
        </div>
        <img className={styles.dropArrow} src={dropArrow} alt='Scroll down for more information'/>
        </div>
    </main>
    )
}

export default Landing;