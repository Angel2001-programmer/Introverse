import styles from "./HomeItem.module.css";
const HomeItem = props => {
    return(
    <div className={styles.container}>
        <img className={styles.logo} src={props.image} alt={props.alt}></img>
        <p className={styles.title}>{props.text}</p>
      </div>
    )
}

export default HomeItem;