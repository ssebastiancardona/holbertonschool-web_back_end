import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const usr = await createUser();
    const photo = await uploadPhoto();
    return {
      photo,
      user,
    };
  } catch (error) {
    return {
      photo: null,
      usr: null,
    };
  }
}
