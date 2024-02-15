import styles from './EditPosts.module.css';
import profile from '../../assets/images/logos/user.png';

const EditPosts = (props) => {
  return (
    <div className={styles.postsContainer}>
      <h2>Posts</h2>
      {props.data.map((post) => (
        <div
          key={post.post_id}
          className={styles.post}
        >
          <div className={styles.postProfilecontainer}>
            <div className={styles.userPhotoContainer}>
              <img
                src={profile}
                alt='profile.'
              />
            </div>
            <div className={styles.userInfocontainer}>
              <h6>{post.post_author}</h6>
              <h6>{post.post_category}</h6>
            </div>
          </div>

          <p className={styles.postContent}>{post.post_content}</p>

          <p>
            {new Date(post.post_date).toLocaleDateString('en-GB', {
              weekday: 'short',
              day: 'numeric',
              month: 'short',
              year: 'numeric',
            })}
          </p>
          <p style={{ margin: '0px', padding: '0px' }}>
            {new Date(post.post_date).toLocaleTimeString('en-GB', {
              hour12: 'true',
            })}
          </p>
          <div className={styles.commentContainer}>
            <img
              className={styles.comment}
              src={require('../../assets/icons/comments.png')}
              alt='comments'
            />
            <p>0</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default EditPosts;
