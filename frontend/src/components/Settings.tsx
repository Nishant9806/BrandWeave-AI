function Settings() {
  return (
    <div className="settings-page">
      <div className="page-heading">
        <div>
          <h1>Settings</h1>
          <p>Manage your workspace and brand review preferences.</p>
        </div>
      </div>

      <section className="settings-section">
        <h2>Workspace Information</h2>

        <div className="settings-field">
          <label>Workspace Name</label>
          <input type="text" value="TechNova" readOnly />
        </div>

        <div className="settings-field">
          <label>Industry</label>
          <input type="text" value="Technology" readOnly />
        </div>

        <div className="settings-field">
          <label>Primary Product</label>
          <input type="text" value="SmartWatch Pro" readOnly />
        </div>
      </section>

      <section className="settings-section">
        <h2>Review Preferences</h2>

        <div className="settings-field">
          <label>Default Content Language</label>
          <select defaultValue="English">
            <option>English</option>
            <option>Hindi</option>
          </select>
        </div>

        <div className="settings-field">
          <label>Review Mode</label>
          <select defaultValue="Hybrid Review">
            <option>Hybrid Review</option>
            <option>Rule-Based Review</option>
            <option>AI Review</option>
          </select>
        </div>

        <div className="settings-field">
          <label>Human Approval Required</label>
          <select defaultValue="Yes">
            <option>Yes</option>
            <option>No</option>
          </select>
        </div>
      </section>

      <div className="settings-note">
        Settings are currently demo configurations. Saving and persistent
        configuration will be connected to the backend later.
      </div>
    </div>
  )
}

export default Settings