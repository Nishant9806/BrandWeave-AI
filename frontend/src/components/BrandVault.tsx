function BrandVault() {
  return (
    <div className="brand-vault-page">

      <div className="page-heading">
        <span className="eyebrow">BRAND KNOWLEDGE CENTER</span>
        <h1>Brand Vault</h1>
        <p>
          Manage and explore the approved identity, facts and
          communication guidelines of TechNova.
        </p>
      </div>

      {/* Brand Identity */}

      <section className="vault-section">
        <h2>Brand Identity</h2>

        <div className="vault-grid">

          <div className="vault-card">
            <span>Brand Name</span>
            <strong>TechNova</strong>
          </div>

          <div className="vault-card">
            <span>Product</span>
            <strong>SmartWatch Pro</strong>
          </div>

          <div className="vault-card">
            <span>Industry</span>
            <strong>Technology</strong>
          </div>

          <div className="vault-card">
            <span>Description</span>
            <strong>Smart device technology brand</strong>
          </div>

        </div>
      </section>

      {/* Approved Facts */}

      <section className="vault-section">
        <h2>Approved Brand Facts</h2>
        <p>Verified product information used during content reviews.</p>

        <table className="vault-table">
          <thead>
            <tr>
              <th>Fact</th>
              <th>Approved Value</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td>Battery Life</td>
              <td>24 hours</td>
              <td>APPROVED</td>
            </tr>

            <tr>
              <td>Product Price</td>
              <td>₹1,499</td>
              <td>APPROVED</td>
            </tr>
          </tbody>
        </table>
      </section>

      {/* Terminology */}

      <section className="vault-section">
        <h2>Terminology Guidelines</h2>

        <table className="vault-table">
          <thead>
            <tr>
              <th>Prohibited Term</th>
              <th>Approved Replacement</th>
              <th>Explanation</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td>Smart Watch Professional</td>
              <td>SmartWatch Pro</td>
              <td>Use the officially approved product name.</td>
            </tr>
          </tbody>
        </table>
      </section>

      {/* Prohibited Claims */}

      <section className="vault-section">
        <h2>Prohibited Marketing Claims</h2>

        <ul className="claims-list">
          <li>
            <strong>India's No. 1</strong>
            <span>Unverified superiority claim.</span>
          </li>

          <li>
            <strong>Guaranteed to transform your life</strong>
            <span>Unsupported guaranteed-benefit claim.</span>
          </li>
        </ul>
      </section>

      {/* Brand Tone */}

      <section className="vault-section">
        <h2>Brand Communication Guidelines</h2>

        <div className="tone-section">
          <div>
            <h4>Required Tone</h4>
            <div className="tone-tags">
              <span>Professional</span>
              <span>Friendly</span>
              <span>Informative</span>
            </div>
          </div>

          <div>
            <h4>Tones to Avoid</h4>
            <div className="tone-tags avoid">
              <span>Aggressive</span>
              <span>Misleading</span>
              <span>Exaggerated</span>
            </div>
          </div>
        </div>
      </section>

      <p className="vault-demo-note">
        Demo Brand Configuration · TechNova
      </p>

    </div>
  )
}

export default BrandVault