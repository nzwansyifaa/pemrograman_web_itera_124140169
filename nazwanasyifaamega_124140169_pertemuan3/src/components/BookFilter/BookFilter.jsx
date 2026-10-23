import PropTypes from "prop-types";
import { STATUS_OPTIONS } from "../../constants.js";

// Filter status dan kolom pencarian
function BookFilter({ statusFilter, searchQuery, onStatusChange, onSearchChange }) {
  return (
    <div className="filter">
      <input
        type="text"
        placeholder="Cari judul atau penulis..."
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
      />
      <select
        aria-label="Filter status"
        value={statusFilter}
        onChange={(e) => onStatusChange(e.target.value)}
      >
        <option value="semua">Semua status</option>
        {STATUS_OPTIONS.map(({ value, label }) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>
    </div>
  );
}

BookFilter.propTypes = {
  statusFilter: PropTypes.string.isRequired,
  searchQuery: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
  onSearchChange: PropTypes.func.isRequired,
};

export default BookFilter;
