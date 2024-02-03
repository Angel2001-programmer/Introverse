import styles from './card.module.css';

const Card = (props) => {
  return (
    <div
      className={styles.card}
      style={{
        background: props.UIcolor,
        borderRadius: props.borderRadius,
        overflowY: props.overflowY,
        minWidth: props.width,
      }}
    >
      {props.children}
    </div>
  );
};

export default Card;
