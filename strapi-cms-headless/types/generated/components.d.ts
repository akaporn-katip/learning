import type { Schema, Attribute } from '@strapi/strapi';

export interface BannerBanner extends Schema.Component {
  collectionName: 'components_banner_banners';
  info: {
    displayName: 'Banner';
  };
  attributes: {
    ImageBanner: Attribute.Media;
  };
}

declare module '@strapi/types' {
  export module Shared {
    export interface Components {
      'banner.banner': BannerBanner;
    }
  }
}
