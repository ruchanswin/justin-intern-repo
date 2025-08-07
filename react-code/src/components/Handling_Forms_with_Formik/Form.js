import { useFormik } from "formik";
import * as Yup from "yup";

const Form = () => {
  const formik = useFormik({
    initialValues: {
      name: "Your name here: ",
      email: "Your email here: ",
    },
    validationSchema: Yup.object({
      name: Yup.string().required("Please enter your name."),
      email: Yup.string().email("Your email is invalid.").required("Please enter your email."),
    }),
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2));
    },
  });

  return (
    <form
      onSubmit={formik.handleSubmit}
      style={{ maxWidth: 400, margin: "2rem auto" }}
    >
      <div>
        <label>Name:</label>
        <input
          name="name"
          type="text"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.name}
        />
        {formik.touched.name && formik.errors.name ? (
          <div style={{ color: "red" }}>{formik.errors.name}</div>
        ) : null}
      </div>

      <div>
        <label>Email:</label>
        <input
          name="email"
          type="email"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.email}
        />
        {formik.touched.email && formik.errors.email ? (
          <div style={{ color: "red" }}>{formik.errors.email}</div>
        ) : null}
      </div>

      <button type="submit" style={{ marginTop: "1rem" }}>
        Submit
      </button>
    </form>
  );
};

export default Form;
