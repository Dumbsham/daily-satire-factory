import mongoose, { Schema, model, models } from 'mongoose';

const UserSchema = new Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
  },
  email: {
    type: String,
    unique: true,
    required: [true, 'Email is required'],
    match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'Invalid email address'],
  },
  password: {
    type: String,
    required: [true, 'Password is required'],
    select: false, // Security: Never return passwords by default!
  },
  comicsGeneratedToday: {
    type: Number,
    default: 0,
  },
  lastGenerationDate: {
    type: Date,
    default: Date.now,
  }
}, {
  timestamps: true,
});

// Prevent Next.js from crashing during hot-reloads
const User = models.User || model('User', UserSchema);

export default User;