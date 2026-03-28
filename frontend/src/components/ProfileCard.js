function ProfileCard({ profile }) {
  return (
    <div style={{ border: "1px solid #ddd", padding: "10px", marginTop: "10px" }}>
      <h3>👤 Profile</h3>
      <p>{profile}</p>
    </div>
  );
}

export default ProfileCard;