function Recommendations({ items }) {
  return (
    <div style={{ border: "1px solid #ddd", padding: "10px", marginTop: "10px" }}>
      <h3>📊 Recommendations</h3>
      <ul>
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default Recommendations;