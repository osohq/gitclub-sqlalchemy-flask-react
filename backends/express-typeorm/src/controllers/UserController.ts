import { getRepository } from "typeorm";
import { NextFunction, Request, Response } from "express";
import { User } from "../entities/User";

export class UserController {
    private userRepository = getRepository(User);

    async one(request: Request) {
        const user = await this.userRepository.findOne(request.params.id);
        await request.oso.authorize(request.user, "show_profile", user);
        return user;
    }
}