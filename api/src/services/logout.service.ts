// import * as boom from '@hapi/boom';

import { redis } from '../utils';

export const logout = async (session: string) => {
  await redis.del(session);

  // const dels = await redis.del(session);
  // if (dels === 0) throw boom.badRequest('Invalid input');
};
