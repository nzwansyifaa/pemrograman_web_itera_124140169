import PropTypes from "prop-types";

// Pilihan status buku
export const STATUS_OPTIONS = [
  { value: "milik", label: "Milik" },
  { value: "baca", label: "Sedang dibaca" },
  { value: "beli", label: "Ingin dibeli" },
];

export const getStatusLabel = (value) =>
  STATUS_OPTIONS.find((opsi) => opsi.value === value)?.label ?? value;

// Bentuk objek buku, dipakai untuk PropTypes
export const bookShape = PropTypes.shape({
  id: PropTypes.string.isRequired,
  judul: PropTypes.string.isRequired,
  penulis: PropTypes.string.isRequired,
  status: PropTypes.string.isRequired,
});
