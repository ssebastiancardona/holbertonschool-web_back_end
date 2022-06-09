import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const obj = {};
  try {
    const usr = await createUser();
    const phot = await uploadPhoto();
    Object.assign(obj, {
      phot,
      usr,
    });
  } catch (err) {
    Object.assign(obj, {
      phot: null,
      usr: null,
    });
  }
  return obj;
}